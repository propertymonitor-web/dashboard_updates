# Waypost, the web page

**Waypost** is a bulletin board system (BBS) that runs over MeshCore radio. This is the page callers use to log in. It runs entirely in your browser and talks to your MeshCore radio over USB or Bluetooth. It sends nothing to any server.

By: Lodestar

## What you need

- Chrome or Edge on a computer, or Chrome on Android. Safari and Firefox cannot talk to radios.
- A MeshCore radio running the companion firmware that matches how you connect: the **USB companion** for the Login button, the **BLE companion** for the Bluetooth button. Close the phone app first: a radio takes only one Bluetooth connection at a time.
- A WAYPOST BBS within reach of your radio. Your radio must have heard its advert so it is in your contacts. Ask the sysop to send an advert if you cannot see it.

## Log in

1. Open the page and press **Login to Waypost** (USB) or **Use Bluetooth instead**.
2. Pick your radio in the browser window.
3. The page finds the BBS (a contact whose name starts with WAYPOST) and takes you in.
4. New here? The BBS asks for a handle: 3 to 12 letters, numbers or underscores. That is your sign-up.

You do not have to use this page. You can also sign up and log in by sending direct messages to the BBS from the MeshCore app. This page just makes it friendlier.

## What you see

- **Menu tiles:** Bulletins, Mail, Boards, Library, Games, Net, Who, Callers, Help, Signal. Press the highlighted letter or click.
- **NEW markers:** the page asks the BBS every 10 minutes whether anything changed (bulletins, mail, new posts, library files, games, an open net check-in). Each check is one small message over the mesh. Press **Check now** any time.
- **Type a command** in the box at the bottom: `?` lists them. Long answers end with a **Next** button.
- **Link:** shows how your messages reached the BBS (direct or hops, and signal strength).

## More than one BBS in range?

If your radio hears several WAYPOST BBS radios, the page lists them. Press **Test signal** to message each one and see its hops, signal and speed, then **Connect to best**. Press **R** (or the BBS radios button) later to switch. BBSes that are linked together share users, mail, scores and same-name public boards, so your handle and scores follow you.

## Sysops

- **Run your own Mesh BBS?** Contact **lodestar_aries@protonmail.com** with the subject line **Waypost BBS** and the County, City and State (or your country's equivalent) where you would like to run your Waypost BBS. The page has a button that writes the email for you.
- **Remote console:** add `?sysop=1` to the page address, connect your own companion radio, and unlock the read-only STATUS view with your remote code. It needs the Waypost BBS program on your PC.

## Good to know

- To point the page at one BBS, add `#bbs=` and the first 12 characters of its public key to the page address.
- **Not tested on real radios yet:** Web Serial and Bluetooth from this page, and the BBS itself, have been tested only against simulated radios. Tell us what you find.
- This folder holds the finished page only. Third-party notices are in `THIRD-PARTY-NOTICES.txt`.

Engineered by Aries Thorne and Todd Steinhauer for Wolf Reactive Systems (WRS). Special thanks to the NTXMESH community, the MeshCore community, and Pat Steinhauer-Scates for their guidance and support.
