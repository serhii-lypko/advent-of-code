const { log } = console;

export default function solution(input: string) {
  let res = 0;

  const actionsMap = {
    "(": (val: number) => val + 1,
    ")": (val: number) => val - 1,
  };

  for (const char of input) {
    res = actionsMap[char as "(" | ")"](res);
  }

  log(res);
}
