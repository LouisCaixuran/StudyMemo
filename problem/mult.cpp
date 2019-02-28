#include<iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int size(long x){
	int count=0;
	while(x){
		count++;
		x=x/10;
	};
	return count;
}
 
int max(int x, int y){
	return x>y?x:y;
}
 
long karatsuba(long x, long y){
	int m;
	long x1,x0;
	long y1,y0;
	long z0,z1,z2;
	if(x<10||y<10)
		return x*y;
	
	m = max(size(x),size(y)) / 2;
 
	x1=x/(int)pow(10,m);
	x0=x-x1*(int)pow(10,m);
	y1=y/(int)pow(10,m);
	y0=y-y1*(int)pow(10,m);

	z2 = karatsuba(x1,y1);
	z0 = karatsuba(x0,y0);
	z1=karatsuba((x1+x0),(y1+y0))-z0-z2;
	long a=z2*pow(10,m*2);
	long b=z1*pow(10,m);
	cout<<"a="<<a<<",b="<<b<<",z0="<<z0;
	return a+b+z0;
}
 
int main(){
	cout<<karatsuba(123456789,987654321);
	return 0;
}
