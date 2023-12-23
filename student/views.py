from drf_spectacular.utils import extend_schema, OpenApiTypes
from rest_framework import viewsets
from rest_framework.response import Response
from .student_choices import GENDER_CHOICES
from rest_framework.decorators import action
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    http_method_names = ['get']

    @extend_schema(responses={200: StudentSerializer(many=True)})
    @action(detail=False, methods=['get'])
    def get_female_students(self, request):
        students = Student.objects.filter(gender='female')
        return Response(self.serializer_class(students, many=True).data)