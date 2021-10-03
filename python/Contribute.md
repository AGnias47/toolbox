# [Simplified Instructions for Submitting a Change to cpython](https://devguide.python.org/)

## One Time Steps

1. Create an account on the [Python Bug Tracker](https://bugs.python.org/user?@template=register) site
2. Fill out and sign the [contributor form](https://www.python.org/psf/contrib/contrib-form/)
3. Fork the [cpython](https://github.com/python/cpython.git) repository

## Issue Specific Changes

1. Unless changing a small typo, etc., submit an issue using the [Bug Tracker](https://bugs.python.org/)
2. Build Python
Linux: ```./configure --with-pydebug && make -j```
3. Run Tests
Linux ```./python -m test -j3```
4. Create an appropriately named branch, ex. ```git checkout -b fix-issue-12345 master```
5. Run ```make patchcheck``` to ensure changes are okay
6. Create a pull request. If an issue was created, refer to the title as "bpo-xxx", ex. bpo-12345: Fix some bug in spam module

