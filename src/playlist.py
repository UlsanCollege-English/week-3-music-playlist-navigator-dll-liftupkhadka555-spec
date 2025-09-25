# /src/playlist.py

class _DNode:
    __slots__ = ("title", "prev", "next")

    def __init__(self, title):
        self.title = title
        self.prev = None
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title):
        """Append a new song at the end of the playlist."""
        node = _DNode(title)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def play_first(self):
        """Set current pointer to the first song. Return its title or None."""
        self.current = self.head
        return self.current.title if self.current else None

    def next(self):
        """Move to the next song if possible. If at tail, stay at tail. Return current title or None."""
        if not self.current:
            return None
        if self.current.next:
            self.current = self.current.next
        return self.current.title

    def prev(self):
        """Move to the previous song if possible. If at head, stay at head. Return current title or None."""
        if not self.current:
            return None
        if self.current.prev:
            self.current = self.current.prev
        return self.current.title

    def insert_after_current(self, title):
        """Insert a new song immediately after the current one. Append at end if no current."""
        node = _DNode(title)
        if not self.current:
            if not self.head:
                self.head = self.tail = node
                self.current = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
        else:
            nxt = self.current.next
            self.current.next = node
            node.prev = self.current
            node.next = nxt
            if nxt:
                nxt.prev = node
            else:
                self.tail = node

    def remove_current(self):
        """Remove the current song and move current to next if possible, else prev. Return True if removed."""
        if not self.current:
            return False  # nothing to remove

        prev_node = self.current.prev
        next_node = self.current.next

        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node

        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node

        # move current pointer
        self.current = next_node if next_node else prev_node

        return True  # song removed

    def to_list(self):
        """Return all song titles from head to tail as a list."""
        result = []
        node = self.head
        while node:
            result.append(node.title)
            node = node.next
        return result
