#!/usr/bin/env python3

import fsm

m = fsm.Machine("hos")

m.header("""
#include <cstdlib>
#include <iostream>
#include <string>
#include <time.h>

using namespace std;

char * now() {
  time_t rawtime;
  time(&rawtime);
  return ctime (&rawtime);
}
""")

m.state('OFF_DUTY',
        '// code for OFF_DUTY_STATE\n',
        [m.edge('END', 'END', """
cout << "th-th-that's all, folks." << endl;
exit(EXIT_SUCCESS);
"""),
         m.edge('ON_DUTY', 'ON_DUTY_STATIONARY', """
cout << "driver coming on duty " << now();
""")])

m.state("ON_DUTY_STATIONARY", 'cout << "driver is stationary" << endl;\n',
        [m.edge("OFF_DUTY",  "OFF_DUTY", 'cout << "driver coming off duty " << now();'),
         m.edge('START', 'ON_DUTY_MOVING')])

m.state('ON_DUTY_MOVING', 'cout << "driver is moving" << endl;\n',
        [m.edge('STOP', 'ON_DUTY_STATIONARY')])

m.state('END', '')

m.footer("""
Event get_next_event() {
   string event_string;
   cin >> event_string;
   return string_to_event(event_string);
}


int main() {
    int result = hos(OFF_DUTY_STATE);
    return result >= 0 ? EXIT_SUCCESS : EXIT_FAILURE;
}
""")

if __name__ == '__main__':
    m.gen()
