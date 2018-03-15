#include "arguments"
void main() {
  ofstream fout(folder["output"] + "/data.txt");
  int n = atoi(parameters["n"].c_str());
  for (int i = 0; i < n; i++) {
    fout << i << endl;
  }
}
