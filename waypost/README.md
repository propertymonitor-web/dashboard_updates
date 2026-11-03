# Waypost, the web page

The Waypost login page for callers of a Waypost BBS. It runs entirely in your browser and talks to your MeshCore radio over USB (Web Serial) or Bluetooth. It sends nothing to any server.

- Use Chrome or Edge on a computer, or Chrome on Android. Safari and Firefox cannot talk to radios.
- Your radio needs the companion firmware that matches the cable: USB companion for the Login button, BLE companion for the Bluetooth button.
- Your radio must have heard the BBS advert so the BBS is in its contact list. The page looks for a contact whose name starts with WAYPOST. To point it at one BBS, add `#bbs=` and the first 12 characters of its public key to the page address.
- Want to run your own Mesh BBS? Contact lodestar_aries@protonmail.com with the subject line "Waypost BBS" and the County, City and State (or your country's equivalent) where you would like to run it.

This folder holds the finished page only. Engineered by Aries Thorne and Todd Steinhauer for Wolf Reactive Systems (WRS). Special thanks to the NTXMESH community, the MeshCore community, and Pat Steinhauer-Scates for their guidance and support.

Not tested on a real radio from GitHub Pages yet: Web Serial and Bluetooth need a real browser and radio.
