def easing(elapsed, start, end, total):
    elapsed /= total
    return  start -end * elapsed * (elapsed - 2);
