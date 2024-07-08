const { log } = console;

import solution from "./day-1.ts";

async function main() {
  const input = await Deno.readTextFile("./input.txt");

  const sol = solution(input);
  // log(sol);
}

main();
