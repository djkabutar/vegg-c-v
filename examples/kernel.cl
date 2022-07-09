


__kernel   void        d_add_matrices 
(float a, float b, float results, int count) {
    int i = get_global_id(0);
    results[i] = a[i] + b[i];
}

// void main() {
//     int a = 5;
// }