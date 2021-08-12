from django.db.models import Count
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import GenericViewSet

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from custom_user.api.permissions import (
    IsOwnerOrStaffOrReadOnly,
    IsAuthenticateAndIsOwner
)
from custom_user.api.serializers import UserProfileSerializer, IgnoreUserSerializer, UserRegisterSerializer, \
    CountrySerializer
from custom_user.models import CustomUser, IgnoreUser, Country
from custom_user.services.email import send
from custom_user.services.remove_user_from_ignore import remove_user_from_ignore


class UserRegisterAPIView(APIView):
    """
    Регистрация пользователя.
    При успешной регистрации отправляем письмо
    """

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send(request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileRetrieveView(mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              GenericViewSet):
    """Вью профиля, с личной информацией и статистикой"""

    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrStaffOrReadOnly, ]
    queryset = CustomUser.objects.all().annotate(
        follow_count=Count('follow'),
    ).select_related('country').prefetch_related('follow', 'user_comment', 'user').order_by('id')
    lookup_field = 'username'

    @action(detail=False, methods=['GET', 'POST'], permission_classes=[IsAuthenticated])
    def ignored_list(self, request):
        """
        Личный игнор лист пользователя.
        При POST запросе проверяем передан ли игнорируемый пользователь.
        Если пользователь передан, то убираем из игнора
        """
        if request.data.get('ignored_user', None) and request.method == 'POST':
            remove_user_from_ignore(request)

        ignore_list = IgnoreUser.objects.filter(user=request.user.id)
        serializer = IgnoreUserSerializer(ignore_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IgnoreUserViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        GenericViewSet):
    """
    API позволяющая игнорировать пользователя.
    Добавлять, просматривать и обновлять может только owner
    """
    serializer_class = IgnoreUserSerializer
    queryset = IgnoreUser.objects.all()
    permission_classes = [IsAuthenticateAndIsOwner, ]


class CountryListView(mixins.ListModelMixin,
                      GenericViewSet):
    """
    API для просмотра стран
    Доступно только администратору
    """
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    permission_classes = [IsAdminUser, ]
