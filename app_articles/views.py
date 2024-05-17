from rest_framework import viewsets

from .models import Category, JournalModel
from .serializers import CategorySerializers, JournalSerializers, JournalGetSerializers
from .permissions import IsAdminReadOnly


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminReadOnly]


class JournalView(viewsets.ModelViewSet):
    queryset = JournalModel.objects.all()
    permission_classes = [IsAdminReadOnly]

    def get_serializer_class(self):
        if self.request.method == "GET" and "pk" not in self.kwargs:
            return JournalGetSerializers
        return JournalSerializers
