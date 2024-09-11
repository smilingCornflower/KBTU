#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

bool isPrime(int n){
    if (n == 1){
        return false;
    }
    
    for (int i = 2; i <= sqrt(n); i++){
        if (n % i == 0){
            return false;
        }
    }
    
    return true;
}

void cntPrimes(vector<int> primes, int n, vector <int> superprimes){

    for (int i = 2; i <= 1000000; i++){ 
        if (isPrime(i) == true){
            primes.push_back(i);
        }
    }

    for (int i = 2; i <= 10000; i++){
        if (isPrime(i) == true){
            superprimes.push_back(primes[i - 1]);
        }
    }

    cout << superprimes[n - 1];
}

int main(){
    int n; cin >> n;
    vector <int> primes;
    vector <int> superprimes;
    cntPrimes(primes, n, superprimes);
}