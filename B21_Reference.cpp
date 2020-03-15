//
// Created by 古家顺 on 2020/3/13.
//

#include <iostream>
using namespace std;

struct stack{  //定义一个栈
    int* Slist;
    int top;
    int Maxsize;
};
void Initstack(stack&SL, int MS); //栈初始化
bool Stackempty(stack&SL);//判栈空
bool Stackfull(stack&SL); //栈满
void Clearstack(stack&SL); //清空栈
int Push(stack&SL, int&item);//新元素推进栈
int Pop(stack&SL);//出栈
void Traverstack(stack&SL); //输出栈中元素



void Initstack(stack&SL, const int MS) //栈的初始化
{
    SL.Slist = new int[MS];
    if (!SL.Slist){
        cout << "给栈分配内存失败。" << endl;
        exit(1);
    }
    SL.Maxsize = MS;
    SL.top = -1;   
}
bool Stackempty(stack&SL) //判空
{
    return SL.top == -1;
}
bool Stackfull(stack&SL)//判满
{
    return SL.top == SL.Maxsize;
}
void Clearstack(stack&SL)//清空栈
{
    SL.top = -1;
}
int Push(stack&SL, int&item)//元素进栈
{
    if (Stackfull(SL)) return false;
    SL.top++;
    SL.Slist[SL.top] = item;
    return SL.Slist[SL.top];
}
int Pop(stack&SL) //元素出栈
{
    if (Stackempty(SL)) return false;
    return SL.Slist[SL.top--];
    SL.top--;
}
void Traverstack(stack&SL)//输出栈
{
    for (int i = 0; i <= SL.top; i++)
        cout << SL.Slist[i] << endl;
    cout << endl;
}




const int N =5;//预设栈的最大空间
int main(){
    cout << "***************商品货架管理****************" << endl;

    int i, t, temp, x;
    stack s;
    Initstack(s, N);
    cout << "输入货架上的现有的商品信息：" << endl;
    cout << "注：从最里端开始（即日期较大），预设货架有五个商品可放空间，输入五组数据，每个商品日期以回车键结束输入" << endl;
    for (i = 0; i<N ;i++) { //输入5个日期
        cin >> x;
        Push(s,x);
    }
    cout << "***************商品录入完毕****************" << endl;

    cout << "请输入要取商品的数量:" << endl;
    cin >> x;
    while (x<0 || x>N){
        cout << "要求的商品数量不合理，请重新输入：" << endl;
        cin >> x;
    }
    for (i = 0; i<x; i++) //取x件商品
        cout << "取出的商品生产日期有:" << Pop(s) << endl;
    t = s.Maxsize - s.top -1;
    cout << "现在货架还能放下" << t << "件商品" << endl;

    stack s1;//建立辅助栈
    Initstack(s1, N);
    cout << "请输入要放入货架的新商品日期：" << endl;
    for(i=0;i<t;i++){//倒货操作
        cin>>x;
        while(Stackempty(s)!=1&&x>s.Slist[s.top]){
            temp=Pop(s);
            Push(s1,temp);
        }
        Push(s,x);
        while(Stackempty(s1)!=1){
            temp=Pop(s1);
            Push(s,temp);
        }
    }
    cout << "***************商品上货完毕****************" << endl;
    cout << "从货架靠里端到外端的商品的日期为:" << endl;
    Traverstack(s); // 显示放入新商品后栈元素顺序

}

