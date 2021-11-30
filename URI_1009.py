#include<iostream>
#include<iomanip>
#include<string>

using namespace std;

int main(){

    string name;
    double s_salary,total_v;

    cin>>name>>s_salary>>total_v;

    cout<<fixed<<setprecision(2)<<"TOTAL = R$ "<<(s_salary+((total_v/100)*15));
    cout<<endl;

    return 0;
}