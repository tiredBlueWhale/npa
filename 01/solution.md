# 1st Assignment Network Protocols and Architectures, WS 25/26

Alex, Luca, Yuho

## Question 1

### a) Draw the C(6).

![C(6)](inet_01.drawio.svg "C(6)")
Fig1 C(6)

### b) Is the topology displayed in Figure 1 a 3-layer Clos topology? Explain your answer.

A 3-layer Clos topology is defined by a leaf layer, a spine layer, and a core layer. In Figure 1 exactly those 3 layers are found

TODO:: Insert graphic

### c) How many switches are required to construct the C(k)? What is the number of hosts? How many links are needed in total?

- Switches: (k/2)^2 * k + k^2
- Hosts:    (K^2)/2
- Links:    (k/2)^2 * k + ((k^3)/2)
