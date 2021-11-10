#!/usr/bin/env python3

import fsm

m = fsm.Machine("float_check")

m.header("""
#include <cctype>
#include <cstdlib>
#include <iostream>
""")

m.state('S0', '', m.edges(('DIGIT', 'S3'),
                          ('SIGN', 'S1'),
                          ('DECIMAL', 'S2')))

m.state('S1', '', m.edges(('DECIMAL', 'S2'),
                          ('DIGIT', 'S3')))

m.state('S2', '', [m.edge('DIGIT', 'S4')])

m.state('S3', '', m.edges(('DIGIT', 'S3'),
                          ('DECIMAL', 'S4'),
                          ('EXPONENT', 'S5')))

m.state('S4', '', m.edges(('DIGIT', 'S4'),
                          ('EXPONENT', 'S5'),
                          ('END_OF_INPUT', 'ACCEPT')))

m.state('S5', '', m.edges(('DIGIT', 'S6'),
                          ('SIGN', 'S7')))

m.state('S6', '', m.edges(('DIGIT', 'S6'),
                          ('END_OF_INPUT', 'ACCEPT')))

m.state('S7', '', [m.edge('DIGIT', 'S6')])

m.state('ACCEPT', """
cout << "Input is valid float" << endl;
return 1;""")

m.footer("""
Event get_next_event() {
  int c;
  while (isspace(c = cin.get())) {
  }
  if (c < 0) {
     return END_OF_INPUT_EVENT;
  }
  if (isdigit(c)) {
    return DIGIT_EVENT;
  }
  if (c == '+' || c == '-') {
    return SIGN_EVENT;
  }
  if (c == '.') {
    return DECIMAL_EVENT;
  }
  if ((c == 'e') || (c == 'E')) {
    return EXPONENT_EVENT;
  }
  return INVALID_EVENT;
};


int main() {
  int result = float_check(S0_STATE);
  cout << "input is " << ((result > 0) ? "valid!" : "INvalid") << endl;
  return result > 0 ? EXIT_SUCCESS : EXIT_FAILURE;
}
""")

m.gen()
