from rest_framework.generics import ListAPIView

from .serializers import FibSerializer
from .models import Fibonacci


class FibApi(ListAPIView):
    serializer_class = FibSerializer

    def get_queryset(self):
        queryset = Fibonacci.objects.all()
        number = self.kwargs['num']
        if number is not None:
            number=int(number)
            num_1 = 1
            num_2 = 1
            if (number < 2):
                fibseries=str(num_1)
            else:
                fibseries=str(num_1)+" "+str(num_2)
                for i in xrange(2, number):
                    temp = num_1 + num_2
                    num_1 = num_2
                    num_2 = temp
                    fibseries+=" "+str(num_2)


            queryset = [{"fib": fibseries, "num": number}]
        return queryset
