#include <iostream>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;
int n;
long long ans;
int a[1000500];
long long int merge(long long int arr[], long long int l, long long int mid, long long int r){
    long long int inv_count = 0;
    long long int n = mid-l+1;
    long long int m = r-mid;
    long long int a[n],b[m],i,j,k;
    for(i=0;i<n;i++)
        a[i] = arr[l+i];
    for(j=0;j<m;j++)
        b[j] = arr[mid+1+j];
    i=0;j=0;k=l;
    while(i<n && j<m){
        if(a[i]<=b[j])
            arr[k++] = a[i++];
        else{
            arr[k++] = b[j++];
            inv_count += n-i;
        }
    }
    while(i<n)
        arr[k++] = a[i++];
    while(j<m)
        arr[k++] = b[j++];
    return inv_count;
}

long long int mergeSort(long long int arr[],long long int l,long long int r){
    long long int inv_count=0;
    if(l<r){
        long long int mid = (l+r)/2;
        inv_count=mergeSort(arr,l,mid);
        inv_count+=mergeSort(arr,mid+1,r);
        inv_count+=merge(arr,l,mid,r);
    }
    return inv_count;
}

int main(){
  cin>>n;
  long long a[n];
  for (int i=0; i<n; i++)
    cin>>a[i];

  cout<<mergeSort(a,0,n-1);
}
