
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

#include <iostream>
using namespace std;

enum State {
  OFF_DUTY_STATE,
  ON_DUTY_STATIONARY_STATE,
  ON_DUTY_MOVING_STATE,
  END_STATE,
};

enum Event {
  END_EVENT,
  ON_DUTY_EVENT,
  OFF_DUTY_EVENT,
  START_EVENT,
  STOP_EVENT,
  INVALID_EVENT
};

const char * EVENT_NAMES[] = {
  "END",
  "ON_DUTY",
  "OFF_DUTY",
  "START",
  "STOP",
};

Event get_next_event();

Event string_to_event(string event_string) {
  if (event_string == "END") {return END_EVENT;}
  if (event_string == "ON_DUTY") {return ON_DUTY_EVENT;}
  if (event_string == "OFF_DUTY") {return OFF_DUTY_EVENT;}
  if (event_string == "START") {return START_EVENT;}
  if (event_string == "STOP") {return STOP_EVENT;}
  return INVALID_EVENT;
}

int hos(State initial_state) {
  State state = initial_state;
  Event event;
  while (true) {
    switch (state) {

      case OFF_DUTY_STATE:
        cerr << "state OFF_DUTY" << endl;
        // code for OFF_DUTY_STATE

        event = get_next_event();
        cerr << "event" << EVENT_NAMES[event] << endl;
        switch (event) {

        case END_EVENT:
          
cout << "th-th-that's all, folks." << endl;
exit(EXIT_SUCCESS);

          state = END_STATE;
          break;

        case ON_DUTY_EVENT:
          
cout << "driver coming on duty " << now();

          state = ON_DUTY_STATIONARY_STATE;
          break;

        default:
          cerr << "INVALID EVENT" << event << "in state OFF_DUTY" << endl;
          return -1;
        }
        break;

      case ON_DUTY_STATIONARY_STATE:
        cerr << "state ON_DUTY_STATIONARY" << endl;
        cout << "driver is stationary" << endl;

        event = get_next_event();
        cerr << "event" << EVENT_NAMES[event] << endl;
        switch (event) {

        case OFF_DUTY_EVENT:
          cout << "driver coming off duty " << now();
          state = OFF_DUTY_STATE;
          break;

        case START_EVENT:
          
          state = ON_DUTY_MOVING_STATE;
          break;

        default:
          cerr << "INVALID EVENT" << event << "in state ON_DUTY_STATIONARY" << endl;
          return -1;
        }
        break;

      case ON_DUTY_MOVING_STATE:
        cerr << "state ON_DUTY_MOVING" << endl;
        cout << "driver is moving" << endl;

        event = get_next_event();
        cerr << "event" << EVENT_NAMES[event] << endl;
        switch (event) {

        case STOP_EVENT:
          
          state = ON_DUTY_STATIONARY_STATE;
          break;

        default:
          cerr << "INVALID EVENT" << event << "in state ON_DUTY_MOVING" << endl;
          return -1;
        }
        break;

      case END_STATE:
        cerr << "state END" << endl;
        
        event = get_next_event();
        cerr << "event" << EVENT_NAMES[event] << endl;
        switch (event) {

        default:
          cerr << "INVALID EVENT" << event << "in state END" << endl;
          return -1;
        }
        break;

    }
  }
}

Event get_next_event() {
   string event_string;
   cin >> event_string;
   return string_to_event(event_string);
}


int main() {
    int result = hos(OFF_DUTY_STATE);
    return result >= 0 ? EXIT_SUCCESS : EXIT_FAILURE;
}
