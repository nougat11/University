#include <iostream>
#include<mmintrin.h>
#include<vector>
using namespace std;
vector<int> solve(_int8 *A, _int8 *B, _int8 *C, _int16 *D) {
	__m64 mm0, mm1, mm2, mm3, mm4, mm5, mm6, mm7;
	mm0 = _mm_setr_pi16(A[0], A[1], A[2], A[3]);
	mm1 = _mm_setr_pi16(A[4], A[5], A[6], A[7]);
	mm2 = _mm_setr_pi16(B[0], B[1], B[2], B[3]);
	mm3 = _mm_setr_pi16(B[4], B[5], B[6], B[7]);
	mm4 = _mm_sub_pi16(mm0, mm2);
	mm5 = _mm_sub_pi16(mm1, mm3);
	mm0 = mm4;
	mm1 = mm5;
	mm2 = _mm_setr_pi16(C[0], C[1], C[2], C[3]);
	mm3 = _mm_setr_pi16(C[4], C[5], C[6], C[7]);
	mm6 = _mm_add_pi16(mm0, mm2);
	mm7 = _mm_add_pi16(mm1, mm3);
	mm0 = _mm_setr_pi32(mm6.m64_i16[0], mm6.m64_i16[1]);
	mm1 = _mm_setr_pi32(mm6.m64_i16[2], mm6.m64_i16[3]);
	mm2 = _mm_setr_pi32(mm7.m64_i16[0], mm7.m64_i16[1]);
	mm3 = _mm_setr_pi32(mm7.m64_i16[2], mm7.m64_i16[3]);
	mm4 = _mm_setr_pi32(D[0], D[1]);
	mm5 = _mm_setr_pi32(D[2], D[3]);
	mm6 = _mm_setr_pi32(D[4], D[5]);
	mm7 = _mm_setr_pi32(D[6], D[7]);
	mm0 = _mm_add_pi32(mm0, mm4);
	mm1 = _mm_add_pi32(mm1, mm5);
	mm2 = _mm_add_pi32(mm2, mm6);
	mm3 = _mm_add_pi32(mm3, mm7);
	vector <int> ans = { mm0.m64_i32[0], mm0.m64_i32[1], mm1.m64_i32[0], mm1.m64_i32[1], mm2.m64_i32[0], mm2.m64_i32[1], mm3.m64_i32[0], mm3.m64_i32[1] };
	return ans;
}
vector<int> solve_simply(_int8* A, _int8* B, _int8* C, _int16* D) {
	vector<int> ans;
	for (int i = 0; i < 8; i++) {
		ans.push_back(A[i] - B[i] + C[i] + D[i]);
	
	}
	return ans;
}

int main()
{
	
	_int8 A[8] = { 7, 8, 5,-127, 0, 0, 0, 0 };
	_int8 B[8] = { 4, 3, 2, 127, 0, 0, 0, 0 };
	_int8 C[8] = { 5, 7, 9, 4, 6, 4, 8, 9};
	_int16 D[8] = { 45, 3213, 21, 123, 13, 312, 123, 12 };
	vector<int> ans1 = solve(A, B, C, D);
	vector<int> ans2 = solve_simply(A, B, C, D);
	
	cout << (bool) (ans1 == ans2);
}


