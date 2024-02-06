# What is SeedSeeker?

SeedSeeker is a project that allows you to select a "Seed", an initial value that is mutated when fuzzing a program.
Many people try to improve their Harness and get more edges in less time by using Coverage-Guided Fuzzing or Redqueen or Radamsa, but they don't pay much attention to the coverage of the seed to mutate.
In my case, when fuzzing the antivirus (Windows Defender), I specified the target function as a function that scans files, and initially provided a bunch of common files as seeds for this, and due to the slower-than-expected Exec speed, I didn't get many edges in the limited time.
So I developed SeedSeeker and analyzed most of the files I use (files with almost every extension you can imagine, plus malware, etc.) as analysis seeds, and when I got the results, I saw that exe files compressed using Packer and .7z had more than double the coverage than other files.
After fuzzing with 10 seed files carefully selected by SeedSeeker, we were able to get 2.3 times more edges than the original seeds in the same amount of time.

#TODO
Rather than just considering the number of basic blocks, I am further developing to consider the code size within a basic block.
