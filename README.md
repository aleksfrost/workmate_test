# workmate_test
## The test task for Workmate

## SCRIPT works as:
### 'python main.py --file products.csv --where "rating>4.5" --aggregate "price=avg" --order-by "rating=desc"'
### where:
#### - '--file' is filename (CSV)
#### - '--where' is the filter (<, > or =)
#### - '--aggregate' is functions (min, max, avg)
#### - '--order-by' range (desc, asc)

### Test file "products.csv" is in repo

## To run tests:
### 1. Install requiremets.txt

# Test 1
```
python main.py --file products.csv --where "rating>4.6" --aggregate "price=avg"
```
```
+-------+
|   avg |
+=======+
|   999 |
+-------+
```

# Test 2
```
python main.py --file products.csv --where "price<500" --order-by "price=desc"
```
```
+---------------+---------+---------+----------+
| poco x5 pro   | xiaomi  |     299 |      4.4 |
+---------------+---------+---------+----------+
| redmi note 12 | xiaomi  |     199 |      4.6 |
+---------------+---------+---------+----------+
| redmi 10c     | xiaomi  |     149 |      4.1 |
+---------------+---------+---------+----------+
```