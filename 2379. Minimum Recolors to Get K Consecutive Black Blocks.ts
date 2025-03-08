function minimumRecolors(blocks: string, k: number): number {
  let start = 0;
  let end = k - 1;

  const blockArray = Array.from(blocks);

  let amountOfW = blockArray.slice(0, k).filter((b) => b === "W").length;

  let minAmount = amountOfW;

  while (end < blocks.length - 1) {
    end += 1;
    amountOfW += blockArray[end] === "W" ? 1 : 0;
    amountOfW -= blockArray[start] === "W" ? 1 : 0;
    start += 1;

    if (amountOfW < minAmount) minAmount = amountOfW;
  }

  return minAmount;
}
