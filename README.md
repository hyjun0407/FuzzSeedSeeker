# What is SeedSeeker?

SeedSeeker is a project that allows you to select a "Seed", an initial value that is mutated when fuzzing a program.
Many people try to improve their Harness and get more edges in less time by using Coverage-Guided Fuzzing or Redqueen or Radamsa, but they don't pay much attention to the coverage of the seed to mutate.
In my case, when fuzzing the antivirus (Windows Defender), I specified the target function as a function that scans files, and initially provided a bunch of common files as seeds for this, and due to the slower-than-expected Exec speed, I didn't get many edges in the limited time.
So I developed SeedSeeker and analyzed most of the files I use (files with almost every extension you can imagine, plus malware, etc.) as analysis seeds, and when I got the results, I saw that exe files compressed using Packer and .7z had more than double the coverage than other files.
After fuzzing with 10 seed files carefully selected by SeedSeeker, we were able to get 2.3 times more edges than the original seeds in the same amount of time.

# How-To-Use

In dynamic_rio_path(in code), write the path to your own drrun.exe file.

In run_process_command, specify the executable command line of the process for which you want to measure coverage. The @@ stands for a file path, which will be replaced with the path to the Seed you want to measure.

```c
Example) Harness.exe -f @@, where @@ is replaced with the Seed file whose coverage you want to measure.
```

The Coverage Dump file is created in C:\CoverageDump and the Seed to measure coverage can be placed in C:\CoverageValidate.(You can change it on code)

You Can Easily change target-module that you want to check coverage,

```c
Check_cov_per_file("mpengine.dll", "C:\\CoverageDump")
```

"mpengine.dll" to other.


# Example
```c
---------------------------------------------------
C:\CoverageDump\vfcompat.dll.cov's Count : 109748
C:\CoverageDump\rpcdump.exe.cov's Count : 105656
C:\CoverageDump\GameScript.7z.cov's Count : 101480
C:\CoverageDump\GameScript.zip.cov's Count : 100359
C:\CoverageDump\Hello.MacroEnabled.docm.cov's Count : 97278
C:\CoverageDump\small_archive.zoo.cov's Count : 90663
C:\CoverageDump\small_archive.tar.cov's Count : 90622
C:\CoverageDump\small_archive.cpio.cov's Count : 90426
C:\CoverageDump\small_archive.a.cov's Count : 89567
C:\CoverageDump\Hello.docx.cov's Count : 89168
C:\CoverageDump\small.pdf.cov's Count : 89013
C:\CoverageDump\small_archive.rz.cov's Count : 88775
C:\CoverageDump\HelloWorld.7z.cov's Count : 88752
C:\CoverageDump\HelloWorld.rar.cov's Count : 88146
C:\CoverageDump\small_archive.lrz.cov's Count : 87831
C:\CoverageDump\small_archive.lzo.cov's Count : 87478
C:\CoverageDump\HelloWorld.egg.cov's Count : 87364
C:\CoverageDump\a.svg.cov's Count : 87296
C:\CoverageDump\HelloWorld.alz.cov's Count : 87085
C:\CoverageDump\altn.hwp.cov's Count : 87057
C:\CoverageDump\HelloWorld.zip.cov's Count : 86762
C:\CoverageDump\comment3.xml.cov's Count : 86643
C:\CoverageDump\HelloWorld.elf.x86-64.cov's Count : 85854
C:\CoverageDump\small_exec.elf.cov's Count : 85537
.
.
.
more....
---------------------------------------------------
```



# TODO

1. Rather than just considering the number of basic blocks, I am further developing to consider the code size within a basic block.
2. adjust Coverage Dump and Validate Path via command arguments
3. etc..
