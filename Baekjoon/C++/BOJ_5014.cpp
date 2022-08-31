#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int F, S, G, U, D;
string err = "use the stairs";

int main() {
	cin >> F >> S >> G >> U >> D;
	vector<int> ans(F + 1, -1);
	ans[S] = 0;
	queue<int> q;
	q.push(S);
	while (!q.empty()) {
		int cur = q.front();
		q.pop();

		if (cur + U <= F) {
			if (ans[cur + U] == -1) {
				ans[cur + U] = ans[cur] + 1;
				q.push(cur + U);
			}
		}
		if (cur - D >= 1) {
			if (ans[cur - D] == -1) {
				ans[cur - D] = ans[cur] + 1;
				q.push(cur - D);
			}
		}
		if (cur + U == G || cur - D == G) {
			break;
		}
	}
	if (ans[G] > -1)
		cout << ans[G];
	else cout << err;
	return 0;
}