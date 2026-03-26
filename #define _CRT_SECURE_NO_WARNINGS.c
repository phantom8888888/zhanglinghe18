#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void main()
{
    int a, b;
    int result;
    int k;

    printf("첫 번째 계산할 값을 입력하세요 ==> ");
    scanf("%d", &a);

    printf("<1>덧셈 <2>뺄셈 <3>곱셈 <4>나눗셈 ==> ");
    scanf("%d", &k);

    printf("두 번째 계산할 값을 입력하세요 ==> ");
    scanf("%d", &b);

    if(k == 1) {
        result = a + b;
        printf(" %d + %d = %d \n", a, b, result);
    }
}
# void main()
# {
#     int a, b;
#     int result;
#     char k;
#
#     printf("첫 번째 계산할 값 ==> ");
#     scanf("%d", &a);
#
#     printf("+ - * / %% ==> ");
#     scanf(" %c", &k);
#
#     printf("두 번째 계산할 값 ==> ");
#     scanf("%d", &b);
#
#     if(k == '+') {
#         result = a + b;
#         printf(" %d + %d = %d \n", a, b, result);
#     }
# }
#
#
#
# if(k == '%') {
#  if(b != 0) {
#         result = a % b;
#         printf(" %d %% %d = %d \n", a, b, result);
#     } else
#         printf(" 0으로 나누면 나머지값이 안됩니다. \n");
# }
#
# if (k == '-') {
# result = a - b;
# printf(" %d - %d = %d \n", a, b, result);
# }
#
# if (k == '*') {
# result = a * b;
# printf(" %d * %d = %d \n", a, b, result);
# }
#
# if (k == '/') {
# if (b != 0) {
# result = a / b;
# printf(" %d / %d = %d \n", a, b, result);
# } else
# printf(" 0으로 나누면 안됩니다. \n");
# }

# void main()
# {
#     printf("%d\n", 123);
# printf("%5d\n", 123);
# printf("%05d\n", 123);
#
# printf("%f\n", 123.45);
# printf("%7.1f\n", 123.45);
# printf("%7.3f\n", 123.45);
#
# printf("%s\n", "Basic-C");
# printf("%10s\n", "Basic-C");
# }