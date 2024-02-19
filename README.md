# video-editor

A simple declarative style video editor in Python 3.11

## IMPORTANT NOTE

A module is made just for myself and no further development is planned. But I would be very happy if you would like to contribute to this project.

Based on the above, the project supports import and export only to MKV format file

## Usage

To edit videos, I need to put videos into any subdirectory of the `videos/` directory. Then create `actions.json` file in directory with your videos and describe what I want to see.

There are some required extensions, and you have to describe them all into the `actions.json` file.

## Actions
### Check extensions

**Required action**. Filters files by extension.

```json5
{
    "action": "check_extension",
    "allowed_extensions": ["..."]  // Enter the video extensions here by joining them with commas
}
```

### Open

**Required action**. Opens the file as VideoFileClip python-object

```json5
{
    "action": "open"
}
```

### Save

**Required action**. Saves the file in the `output_directory` directory with its own name.

```json5
{
    "action": "save",
    "output_directory": "edited"  // Enter the name of the output folder here
}
```

### Trimming
If I need to trim a video from first second to third second I have to use `cut` action.

```json5
[
  {
    "action": "check_extension",
    "allowed_extensions": ["mkv"]
  },
  {
    "action": "open"
  },
  {
    "action": "cut",
    "start": 1,
    "end": 3
  },
  {
    "action": "save",
    "output_directory": "edited"
  }
]
```


## TODO:
 - Skip the directory if there is no required actions