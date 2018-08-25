# 4-four

Thanks to the wonderful mathematic explanation of Matt Parker in the
[video](https://www.youtube.com/watch?v=LYKn0yUTIU4) where he explained that the
number 4 is the only number that has the same number of letters as its value in
some languages, such as DE, NL and EN.

> _"4 is is a fixed point, it doesn't go anywhere. It maps to itself."_<br/>
> _- Matt Parker_

Matt explained that no matter what number you would take, it would always end up
at the number 4. So I wrote a script that uses his logic from the video in a
function that shows the output of the sequence to test wether it is true or not.

Example run:

```
$ ./four.py 847193 en
==============================
STARTING SEQUENCE
starting number => 847.193
==============================
847.193 => eight hundred and forty-seven thousand, one hundred and ninety-three => 57
57 => fifty-seven => 10
10 => ten => 3
3 => three => 5
5 => five => 4
==============================
```

# Getting started

```
$ git clone https://github.com/kkoomen/4-four.git
$ cd 4-four
$ pip3 install virtualenv
$ virtualenv .
$ source bin/activate
$ pip3 install -r requirements.txt
```
