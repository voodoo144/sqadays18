#!/bin/python
import requests
import unittest

# Before test we should put our test data to etcd server
# ./etcdctl set test-user "Ivan"
# or curl http://localhost:2379/v2/keys/test-user -XPUT -d value="Ivan"
# Then in tests we will get this value

class TestEtcdData(unittest.TestCase):
  
  def setUp(self):
      self.testUser=requests.get('http://localhost:2379/v2/keys/test-user')
      
  def test_get_data(self): 
      self.assertEqual(self.testUser.json()['node']['value'], 'Ivan')

if __name__ == '__main__':
    unittest.main()
