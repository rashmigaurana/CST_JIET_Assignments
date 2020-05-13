#include<iostream>
using namespace std;
int floorSqrt(int A)
{
	if(A==0 || A==1)
	return A;
	int i,result;
	i=1;
	result=1;
	while (result<=A)
	{
		i++;
		result=i*i;
	}
	 return i-1;
}
 
int main()
{
	int A;
	cout<<"enter value of A"<<endl;
	cin>>A;
	cout<<floorSqrt(A)<<endl;
	return 0;
}
