#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
int map[1002][1002];
int n, r, c;

pair<int, int> find() {
	memset(map, 0, sizeof(map));
	int dir = 0;//1:열+1, 2:행+1, 3:열-, 4:행-
	int num = 1;
	int row = 1, col = 1;
	while (num != n) {
		//cout << "(" << row << "," << col << ")\n";
		map[row][col] = num;
		num++;
		if (dir % 4 == 0) {
			if (col + 1 > c || map[row][col+1] != 0) {
				dir++;
				row++;
			}
			else {
				col++;
			}
		}
		else if (dir % 4 == 1) {
			if (row + 1 > r || map[row+1][col] != 0) {
				dir++;
				col--;
			}
			else {
				row++;
			}
		}
		else if (dir % 4 == 2) {
			if (col - 1 < 1 || map[row][col - 1] != 0) {
				dir++;
				row--;
			}
			else {
				col--;
			}
		}
		else {
			if (row - 1 < 1 || map[row - 1][col] != 0) {
				dir++;
				col++;
			}
			else {
				row--;
			}
		}
	}
	return { row,col };
}

int main() {
	cin >> r >> c;
	cin >> n;
	if (r * c < n) {
		cout << 0;
		return 0;
	}
	pair<int,int> ans = find();
	cout << ans.first << " " << ans.second << "\n";
	//for (int i = 1; i <= r; i++) {
	//	for (int j = 1; j <= c; j++) {
	//		cout << map[i][j]<<" ";
	//	}
	//	cout << "\n";
	//}
	return 0;
}