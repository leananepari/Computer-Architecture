"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0

    def load(self, filename):
        """Load a program into memory."""
        try:
            address = 0
            with open(filename) as f:
                for line in f:
                    # Ignore comments
                    comment_split = line.split("#")
                    num = comment_split[0].strip()
                    if num == "":
                        continue

                    value = int(num, 2) #base 2, adds 0b in front
                    self.ram[address] = value
                    address += 1

        except FileNotFoundError:
            print(f"{filename} not found")
            sys.exit(2)


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()
    
    def ram_read(self, address):
      return self.ram[address]
      
    def ram_write(self, value, address):
      self.ram[address] = value

    def run(self):
        """Run the CPU."""
        LDI = 0b10000010
        PRN = 0b01000111
        HLT = 0b00000001
        while True:
          IR = self.ram[self.pc]
          operand_a = self.ram_read(self.pc + 1)
          operand_b = self.ram_read(self.pc + 2)
          if IR == LDI:
            self.reg[operand_a] = operand_b
            self.pc += 3
          elif IR == PRN:
            print(self.reg[operand_a])
            self.pc += 2
          elif IR == HLT:
            break
          else:
            print(f"Error: Unknown command: {IR}")
            break
          

cpu = CPU()

# cpu.load()
# cpu.trace()
# cpu.run()
# print('REG ', cpu.reg)

