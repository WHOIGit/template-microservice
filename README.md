# IFCB ROI microservice

### Description

Given a ROI ID, returns a base64-encoded ROI image and a small amount of technical metadata

### URL pattern

* POST: `/roi-image`
* GET: `/roi-image/{pid}`

### Example POST payload

```json
{
  "pid": "D20230412T123456_IFCB10_00341"
}
```

### Example GET URL

`/roi-image/D20230412T123456_IFCB10_00341`

### Example output

```json
{
  "pid": "D20230412T123456_IFCB10_00341",
  "bin-pid": "D20230412T123456_IFCB10",
  "content-type": "image/png",
  "image": "{base64 encoded PNG}"
}
```

