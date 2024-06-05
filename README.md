# Typing Speed and Error Checker

This script aims to measure how fast you type and count the number of errors made in typing a given prompt.

## How it works

1. The script displays a `bash` prompt, inviting you to type something.
2. It measures the duration of their typing of the prompt.
3. It calculates your typing speed in words per minute.
4. It estimates the total mistakes on your typed input against the prompt given.

## Functions

### TypeError(prompt)

- **Description:** Compares a user's input with the prompt and counts how many mistakes have been made.
- **Parameters**:
  - `prompt` (str): Prompt to enter the text into.
- **Return:**
  - `errors` (int): The number of errors in the user's input.

### speed(inprompt, stime, etime)

- **Description:** It works out the rate at which the user could type in words per minute.
- **Parameters**:
  - `inprompt` (str): The user's input.
  - `stime` (float): The start time.
  - `etime` (float): due time.
- **Returns:**
  - `speed` (float): Speed in words per minute.

### elapsed_time(stime, etime)

- **Description:** Adds up all the durations.
- **Parameters:
  - `stime` (float): the start time.
  - `etime`  : Ending time.
- **Yields
  - `time`: the total amount of time that has elapsed.

## Usage

Run the same script and follow your instructions. The script should give you a prompt to type. On completion of the prompt, it will then show your speed, the time it took you, and the errors you made.

```python
if __name__
Prompt = "Able was I ere I saw Elba: This palindrome contains many common and less common letters, which can help you improve your precision."
print(f" Type this: - {prompt} ")
input("Press Enter when you will be ready to check your speed .!!! ")
stime = time()
in_prompt = input()
etime = time()
time = elapsedime(stime
speed = speed(inprompt,
errors = TypeError(prompt)
print("***************************************************************")
print(f" Total time elapsed {time} seconds                          ")
print(f" Your Average Typing speed was {speed} words per minute(w/m)")
print(f" With the total of {errors} errors                          ")
print("***************************************************************")
```
