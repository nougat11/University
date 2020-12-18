#include <iostream>
#include <mmintrin.h>
#include<vector>
#include<tuple>
using namespace std;
pair<__m64, __m64> push_8(_int8* A) {
	__m64 mm0 = _mm_setr_pi8(A[0], A[1], A[2], A[3], A[4], A[5], A[6], A[7]);
	__m64 mm1 = _mm_setzero_si64();
	__m64 mm2 = _mm_cmpgt_pi8(mm1, mm0);
	mm1 = _m_punpcklbw(mm0, mm2);
	mm2 = _m_punpckhbw(mm0, mm2);
	return make_pair(mm1, mm2);

}
tuple <__m64, __m64, __m64, __m64> unpack16_32(pair<__m64, __m64> a) {
	__m64 zero = _mm_setzero_si64();
	pair<__m64, __m64> mask_zero = make_pair(_mm_cmpgt_pi16(zero, a.first), _mm_cmpgt_pi16(zero, a.second));
	tuple<__m64, __m64, __m64, __m64> ans = make_tuple(_m_punpcklwd(a.first, mask_zero.first), _m_punpckhwd(a.first, mask_zero.first), _m_punpcklwd(a.second, mask_zero.second), _m_punpckhwd(a.second, mask_zero.second));
	return ans;
}
tuple<__m64, __m64, __m64, __m64> push_16(_int16* A) {
	pair <__m64, __m64> mask = make_pair(_mm_setr_pi16(A[0], A[1], A[2], A[3]), _mm_setr_pi16(A[4], A[5], A[6], A[7]));
	return unpack16_32(mask);
}
vector<int> convert_to_int_32(vector <__m64> a) {
	vector<int> b;
	for (int i = 0; i < a.size(); i++)
	{
		b.push_back(a[i].m64_i32[0]);
		b.push_back(a[i].m64_i32[1]);
	}
	return b;

}
vector <int> mmx_solve(_int8* A, _int8* B, _int8* C, _int16* D) {
	pair<__m64, __m64> MMX_A = push_8(A);
	pair<__m64, __m64> MMX_B = push_8(B);
	pair<__m64, __m64> MMX_AB = make_pair(_mm_sub_pi16(MMX_A.first, MMX_B.first), _mm_sub_pi16(MMX_A.second, MMX_B.second));
	pair<__m64, __m64> MMX_C = push_8(C);
	pair<__m64, __m64> MMX_ABC = make_pair(_mm_add_pi16(MMX_AB.first, MMX_C.first), _mm_add_pi16(MMX_AB.second, MMX_C.second));
	tuple <__m64, __m64, __m64, __m64> MMX_ABC_32 = unpack16_32(MMX_ABC);
	tuple<__m64, __m64, __m64, __m64> MMX_D = push_16(D);
	vector <__m64>  ANS{ _mm_add_pi32(get<0>(MMX_ABC_32), get<0>(MMX_D)), _mm_add_pi32(get<1>(MMX_ABC_32), get<1>(MMX_D)), _mm_add_pi32(get<2>(MMX_ABC_32), get<2>(MMX_D)), _mm_add_pi32(get<3>(MMX_ABC_32), get<3>(MMX_D)) };
	return convert_to_int_32(ANS);
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
	__m64 mm0, mm1, mm2, mm3, mm4, mm5, mm6, mm7;
	_int8 A[8] = { 127, 8, 5,-127, 3, 4, 1, 5 };
	_int8 B[8] = { -127, 3, 2, 127, 5, 1, 2, 3 };
	_int8 C[8] = { 127, 5, 3, 1, 4, 2, 4, 1 };
	_int16 D[8] = { 32700, 2, 3, 4, 5, 6, 7, 8 };
	vector<int> ans1 = solve_simply(A, B, C, D);
	vector<int> ans2 = mmx_solve(A, B, C, D);
	for (int i = 0; i < 8; i++)
		cout << ans1[i] << ' ';
	cout << endl;
	for (int i = 0; i < 8; i++)
		cout << ans2[i] << ' ';
	cout << endl<<(bool)	(ans1 == ans2);
	
	


	
	

	

    
    
}
