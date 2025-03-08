function closestPrimes(left: number, right: number): number[] {
  let res = [-1, -1];
  let diff = Number.MAX_SAFE_INTEGER;

  const primes = primeSiv(left, right);

  let index = 1;
  while (index < primes.length) {
    const first = primes[index - 1];
    const second = primes[index];

    if (second - first < diff) {
      res = [first, second];
      diff = second - first;
    }

    index += 1;
  }

  return res;
}

function primeSiv(start: number, end: number): number[] {
  const siv = getSiv(end);

  let iterator = 2;
  while (iterator <= Math.sqrt(end)) {
    if (!siv[iterator]) {
      iterator += 1;
      continue;
    }

    let tmpIterator = iterator * 2;
    while (tmpIterator <= end) {
      siv[tmpIterator] = 0;
      tmpIterator += iterator;
    }

    iterator += 1;
  }

  return siv.reduce((res: number[], curr: number, currIndex: number) => {
    if (curr && currIndex >= start) return [...res, currIndex];
    return res;
  }, []);
}

function getSiv(end: number): number[] {
  let siv: number[] = new Array(end + 1).fill(1);

  siv[0] = 0;
  siv[1] = 0;

  return siv;
}
