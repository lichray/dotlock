import os
from multiprocessing import Process
import unittest
import time

from dotlock import DotLock


class TestSimple(unittest.TestCase):

    def test_single_proc(self):
        with DotLock('single.lock') as lock:
            self.assertTrue(os.path.exists('single.lock'))
            self.assertEqual(repr(lock), "<DotLock: 'single.lock'>")

        self.assertFalse(os.path.exists('single.lock'))

    def test_dbl_unlock(self):
        with DotLock('single.lock') as lock:
            pass

        self.assertRaises(OSError, lock.release)

    def test_excl_lock(self):
        def f():
            lock = DotLock('cross.lock')
            time.sleep(.5)
            self.assertFalse(lock.try_acquire())

        p = Process(target=f)
        p.start()

        with DotLock('cross.lock'):
            p.join()

    def test_blocking(self):
        def f():
            with DotLock('cross.lock'):
                time.sleep(.5)

        p = Process(target=f)
        p.start()
        p.join(.1)

        with DotLock('cross.lock'):
            self.assertFalse(p.is_alive())

        p.join()

    def test_other_errors(self):
        lock = DotLock('not-exists/.lock')
        self.assertRaises(OSError, lock.acquire)
