import os

# Set environment variables
os.environ['DB_NAME'] = "dfnluk6suf5ht3"
os.environ['DB_USER'] = 'vjzkqkklmkxngl'
os.environ['DB_PASSWORD'] = '98e9fc6f5bd1f8f3551aa1b17f3bc2a6307e54dd75598ffbc519d1d9d3d37757'
os.environ['DB_HOST'] = 'ec2-46-137-84-173.eu-west-1.compute.amazonaws.com'
os.environ['DB_PORT'] = '5432'
os.environ['SECRET_KEY'] = 'tf$kn90ndbze3%z6gc(*!)nq#e_^)(h580&do-r9&vt49pte$g'

# Get environment variables
USER = os.getenv('DB_NAME')
PASSWORD = os.environ.get('DB_PASSWORD')