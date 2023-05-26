#include <stdio.h>

double calc(double x[], char z[], int n);

int main()
{
    int n;
    printf("How many values you want to input ?\n");
    scanf("%d", &n);

    double value[n];
    char op[n-1];
    double ans;

    printf("Enter the values with operator\n");
    for (int i = 0; i < n; i++)
    {
        scanf("%lf", &value[i]);
        if (i==(n-1))
        {
            break;
        }
        scanf("%c", &op[i]);
    }

    ans = calc(value,op,n);
    printf("The answer is: %.8lf\n", ans);
    return 0;
}

double calc(double x[], char z[], int n)
{
    double ans = 0;

    char y[(n-1)];
    for (int i = 0; i < (n-1); i++)
    {
        y[i]=z[i];
    }
    
    for (int i = 0; i < (n-1); i++)
    {
        if (y[i]=='/' && z[i-1]=='/')
        {
            x[i+1] = (x[i-1] / x[i+1]);
            x[i-1] = 0;
            y[i] = '+';
        }
        else if (y[i]=='/')
        {
            x[i] = (x[i] / x[i+1]);
            x[i+1] = 0;
            y[i] = '+';
        }
    }
    for (int i = 0; i < (n-1); i++)
    {
        if (y[i]=='*' && z[i-1]=='/')
        {
            x[i+1] = (x[i-1] * x[i+1]);
            x[i-1] = 0;
            y[i] = '+';
        }
        else if (y[i]=='*')
        {
            x[i+1] = (x[i] * x[i+1]);
            x[i] = 0;
            y[i] = '+';
        }
    }
    for (int i = 0; i < n; i++)
    {
        ans += x[i];
    }
    for (int i = 0; i < (n-1); i++)
    {
        if (y[i]=='-' && x[i+1]==0)
        {
            ans -= x[i+2]*2;
        }
        else if (y[i]=='-')
        {
            ans -= x[i+1]*2;
        }
    }
    
    return ans;
}
