#!/usr/bin/env python3

class Machine:
  #initiates machine with name and optional filename
  def __init__(self, name, filename="CCode.cpp"):
    self.name = name
    self.filename = filename
    #storage of all the states and their edges
    self.bank = []
    self.uniqueEdges = []

  
  def header(self, text):
    self.headerString = text

  def footer(self, text):
    self.footerString = text

  #appends every new state to a bank array
  def state(self, state_name, action_string, edge_list=""):
    self.bank.append([state_name, action_string, edge_list])

  def edge(self, event_name, next_state, optional_action_string=""):
    if event_name not in self.uniqueEdges:
      self.uniqueEdges.append(event_name) 
    return [event_name, next_state, optional_action_string]    

  #generates entire C++ file
  def gen(self):
    with open(self.filename, 'w') as f:
      f.write(self.headerString + '\n')
    with open(self.filename, 'a') as f:
      f.write("#include <iostream>\n")
      f.write("using namespace std;\n\n")
      #creates state enum
      f.write("enum State {\n")
      for i in self.bank:
        f.write("  " + i[0] + "_STATE,\n")
      f.write("};\n\n")
      
      #creates event enum
      f.write("enum Event {\n")
      for i in self.uniqueEdges:
        f.write("  " + i + "_EVENT,\n")
      f.write("  INVALID_EVENT\n")
      f.write("};\n\n")
      
      #creates event names
      f.write("const char * EVENT_NAMES[] = {\n")
      for i in self.uniqueEdges:
        f.write("  \"" + i + "\"" + ",\n")
      f.write("};\n\n") 

      #get next event
      f.write("Event get_next_event();\n\n")

      #string to event
      f.write("Event string_to_event(string event_string) {\n")
      for i in self.uniqueEdges:
        f.write("  if (event_string == \"" + i + "\") {return " + i + "_EVENT;}\n")
      f.write("  return INVALID_EVENT;\n}\n\n")      
      
      #the machine
      f.write("int " + self.name + "(State initial_state) {\n")
      f.write("  State state = initial_state;\n")
      f.write("  Event event;\n")
      f.write("  while (true) {\n")
      f.write("    switch (state) {\n\n")
      
      #the actual loop
      for i in self.bank:
        f.write("      case " + i[0] + "_STATE:\n")  
        f.write("        cerr << \"state " + i[0] + "\" << endl;\n")
        f.write("        " + i[1] + "\n") 
        f.write("        event = get_next_event();\n")
        f.write("        cerr << \"event\" << EVENT_NAMES[event] << endl;\n")
        f.write("        switch (event) {\n\n")
        for j in i[2]:
          f.write("        case " + j[0] + "_EVENT:\n")
          f.write("          " + j[2] + "\n")
          f.write("          state = " + j[1] + "_STATE;\n")
          f.write("          break;\n\n")
        f.write("        default:\n")
        f.write("          cerr << \"INVALID EVENT\" << event << \"in state " + i[0] + "\" << endl;\n")
        f.write("          return -1;\n")
        f.write("        }\n")
        f.write("        break;\n\n")
      f.write("    }\n")
      f.write("  }\n")
      f.write("}\n")          
      
    #footer
    with open(self.filename, 'a') as f:
      f.write(self.footerString)

  def edges(self, *args_list):
    array = []
    for i in args_list:
      array.append(self.edge(i[0], i[1]))
    return array





