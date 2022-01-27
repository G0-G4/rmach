# register machine emulator

machine has infinite registers. Each register holds a natural number. All registers hold 0 by default.

## set of instructions

1) Z(n) - clear register n (n could be a number or register name) e.g. Z(1),  Z('i')
2) S(n) - add 1 to register contents
3) T(m, n) - copy contents of register m to register n
4) J(m, n, q) - if contents of register m and n are equal, jump to instruction under number q. Label could be used instead of instruction number.
