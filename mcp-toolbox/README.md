# MCP Server Setup


## Step 1: Set up your database

1. Setup my-sql database in your local
```sql
CREATE DATABASE mcp-connect
```

2. create table
```sql
CREATE TABLE hotels (
  id            INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name          VARCHAR(255) NOT NULL,
  location      VARCHAR(255) NOT NULL,
  price_tier    VARCHAR(255) NOT NULL,
  checkin_date  DATE NOT NULL,
  checkout_date DATE NOT NULL,
  booked        BOOLEAN NOT NULL
);
```


3. Insert data into the table
```sql
INSERT INTO hotels(id, name, location, price_tier, checkin_date, checkout_date, booked)
VALUES
  (1, 'Hilton Basel', 'Basel', 'Luxury', '2024-04-22', '2024-04-20', FALSE),
  (2, 'Marriott Zurich', 'Zurich', 'Upscale', '2024-04-14', '2024-04-21', FALSE),
  (3, 'Hyatt Regency Basel', 'Basel', 'Upper Upscale', '2024-04-02', '2024-04-20', FALSE),
  (4, 'Radisson Blu Lucerne', 'Lucerne', 'Midscale', '2024-04-24', '2024-04-05', FALSE),
  (5, 'Best Western Bern', 'Bern', 'Upper Midscale', '2024-04-23', '2024-04-01', FALSE),
  (6, 'InterContinental Geneva', 'Geneva', 'Luxury', '2024-04-23', '2024-04-28', FALSE),
  (7, 'Sheraton Zurich', 'Zurich', 'Upper Upscale', '2024-04-27', '2024-04-02', FALSE),
  (8, 'Holiday Inn Basel', 'Basel', 'Upper Midscale', '2024-04-24', '2024-04-09', FALSE),
  (9, 'Courtyard Zurich', 'Zurich', 'Upscale', '2024-04-03', '2024-04-13', FALSE),
  (10, 'Comfort Inn Bern', 'Bern', 'Midscale', '2024-04-04', '2024-04-16', FALSE);
```

## Step 2: Install and Configure MCP Toolbox

1. Download latest version of toolbox binary
```python
export OS="linux/amd64" # one of linux/amd64, darwin/arm64, darwin/amd64, or windows/amd64
curl -O https://storage.googleapis.com/genai-toolbox/v0.10.0/$OS/toolbox
```
2. Make the binary executable

```python
chmod +x toolbox
```
3. Add tools.yaml file and configure the database settings

4. Run the toolbox

```python
./toolbox --tools-file "tools.yaml"
```
