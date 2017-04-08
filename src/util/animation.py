def easing(elapsed, start, end, total):
    elapsed /= total
    return -end * elapsed * (elapsed - 2) + start;
