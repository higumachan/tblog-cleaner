# tblog-cleaner

This is a tool that makes it easy to delete a small amount of tensorboard logdir.

# Install

```bash
pip install git+https://github.com/higumachan/tblog-cleaner.git
```

# Usage

```
logs/
├── version_1(big log over 1000 points)
└── version_2(small log under 5 points)
```

```
tblog-cleaner --logsdir logs --tag loss  
```

```
logs/
└── version_1(big log over 1000 points)
```
