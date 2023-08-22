# Quick Start

`Mosaic-Benchmark` is a python library that allows to create modular linkstreams which can be used in format. 


## Tutorial

Creating modular linkstreams using `Mosaic-Benchmark` is easy as this:

``` python
from mosaic_benchmark import ModularLinkStream
M=ModularLinkStream(number_of_nodes=10, t_start=0,t_end=4)
M.add_community([0,1,2,3,4],0,4)
M.add_community([5,6,7,8,9],0,4)
M.generate_edges(1,0,1,0)
M.export('Address:\\')
```

Of course, you can choose among all the algorithms available for scenario description(taking
care of specifying the correct parameters): in any case, you'll get as
a result a '.csv' file for temporal edges and communities as '.npy' file.

You can also perform the action of emptying mosaics using:

``` python
M.empty_mosaics(gamma=0.5)
```

Or you can rewire the edges:

``` python
M.rewiring_noise(eta=0.1)
```

Moreover, you can also visualize communities.

``` python
M.plot()
```

I know, plain tutorials are overrated: if you want to explore `Mosaic-benchmark`
functionalities, please start playing around with our interactive
[Google Colab
Notebook](https://colab.research.google.com/drive/1_H0OU6LU_koyQnbJhS_P5DwC34U00hcG?usp=sharing)!

## FAQ

**Q1.** I developed a novel Scenario description or generating edges method and I would like to see it
integrated in `Mosaic-Benchmark`. What should I do?

**A1.** That's great! Just open an issue on the project
[GitHub](https://github.com/YasAsgari/Mosaic-benchmark) briefly describing the
method (provide a link to the paper where it has been firstly
introduced) and links to a python implementation (if available). We'll
came back to you as soon as possible to discuss the next steps.

**Q2.** Can you add method XXX to your library?

**A2.** It depends. Do you have a link to a python implementation/are
you willing to help us in implementing it? If so, that's perfect. If
not, well... everything is possible but it is likely that it will
require some time.
