#include<iostream>
using namespace std;

int main(){
    int array[6]; 
    cout<<"Enter the Array values"<<endl;
    for(int i = 0; i < 6; i++){ 
        cin>>array[i];
    }
    cout<<endl;
    cout<<"Values in the Array = ";
    for(int j = 0; j < 6; j++){ 
        cout<<array[j]<<" ";
    }
    return 0;
}