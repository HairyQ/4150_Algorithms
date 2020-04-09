#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>

using namespace std;

int main()
{
  string line;
  map <int, vector<int>> dict;
  priority_queue<int> q;
  int N, T;

  //Read first line
  getline(cin, line);

  size_t pos = line.find(" ") + 1;
  N = stoi(line.substr(0, pos - 1));
  line.erase(0, pos);
  T = stoi(line);

  //Read in data, fill data structures appropriately
  int i, deposit, priority;
  int maxTime = 0;
  for (i = 0; i < N; i++)
    {
      getline(cin, line);

      size_t pos = line.find(" ") + 1;
      deposit = stoi(line.substr(0, pos - 1));
      line.erase(0, pos);
      priority = stoi(line);
      if (maxTime < priority)
	maxTime = priority;

      //Add map entry
      if (dict.count(priority) == 0) //not found
	{
	  vector<int> value;
	  value.push_back(deposit);
	  dict.insert(pair<int, vector<int>>(priority, value));
	}
      else //found
	{
	  map<int, vector<int>>::iterator it = dict.find(priority);
	  it -> second.push_back(deposit);
	}
    }

  int total = 0;
  
  // Should have all input - run algorithm
  for (i = maxTime; i >= 0; i--)
    {
      if (dict.count(i) == 0)
	{
	  if (q.empty()) {continue;}
	  else
	    {
	      total += q.top();
	      q.pop();
	    }
	}
      else
	{
	  vector<int> listAtPriority = dict.at(i);
	  for (int j = 0; j < listAtPriority.size(); j++)
	    {
	      q.push(listAtPriority[j]);
	    }
	  total += q.top();
	  q.pop();
	}
    }

  cout << total << endl;
}

