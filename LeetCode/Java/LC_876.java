public class LC_876 {
    public ListNode middleNode(ListNode head) {
        int middle = getMiddle(head);

        int cnt = 0;
        for (int i = 0; i < middle; i++) {
            head = head.next;
        }

        return head;
    }

    public int getMiddle(ListNode head) {
        int size = getSize(head);

        return (int) Math.ceil(size / 2.0);
    }

    public int getSize(ListNode head) {
        int cnt = 0;

        while (head.next != null) {
            head = head.next;
            cnt++;
        }

        return cnt;
    }

    public class ListNode {
        int val;
        ListNode next;

        ListNode() {}

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }
}
