function checkPowersOfThree(n: number): boolean {
  return ![...n.toString(3)].some((c) => c === "2");
}
