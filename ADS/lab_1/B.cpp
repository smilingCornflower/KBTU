#include <iostream>
#include <vector>

using namespace std;

int main(){
    int number;
    cin >> number;

    vector<int> numbers;
    vector<int> answer;

    for (int i = 0; i < number; i++) {
        int x;
        cin >> x;
        numbers.push_back(x);
    }
    answer.push_back(-1);
    
    for (int i = 1; i < number; i++) {
        for (int j = i - 1; j >= 0; j--) {
            if (numbers[i] >= numbers[j]) {
                answer.push_back(numbers[j]);
                break;
            }
            else if (j == 0) {
                answer.push_back(-1);
            }
        }
    }

    for (int i = 0; i < number; i++) {
        cout << answer[i] << " ";
    }
    
}